FROM nvidia/cuda:11.6.2-devel-ubuntu20.04
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update && apt install -y python3-pip && apt upgrade -y
# RUN wget -P /mnt https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# RUN bash /mnt/Miniconda3-latest-Linux-x86_64.sh -b
# ENV PATH=/root/miniconda3/bin:${PATH}
# RUN conda init 
# RUN conda update -y conda && conda install pip pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch